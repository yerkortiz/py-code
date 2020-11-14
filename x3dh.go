package main

import (
    signal "golang.org/x/crypto/ed25519"
	"fmt"
	//signal "github.com/dosco/libsignal-protocol-go"
)

func main() {
	fmt.Printf("hola")
	idA := signal.GenerateRegistrationId()

    msA := signal.NewMemoryStore()
    msB := signal.NewMemoryStore()

    // Alice keys
    idA := signal.GenerateRegistrationId()
    msA.PutLocalRegistrationID(idA)


    ikpA := signal.GenerateIdentityKeyPair()
    msA.PutIdentityKeyPair(ikpA)

    pkA := signal.GeneratePreKey(1)
    msA.PutPreKey(1, pkA)

    spkA := signal.GenerateSignedPreKey(ikpA, 1)
    msA.PutSignedPreKey(1, spkA)

    // Bob keys

    idB := signal.GenerateRegistrationId()
    msB.PutLocalRegistrationID(idB)

    ikpB := signal.GenerateIdentityKeyPair()
    msB.PutIdentityKeyPair(ikpB)

    pkB := signal.GeneratePreKey(1)
    msB.PutPreKey(1, pkB)

    spkB := signal.GenerateSignedPreKey(ikpB, 1)
    msB.PutSignedPreKey(1, spkB)

    fmt.Printf("== Long-term keys\n")

    fmt.Printf("Alice ID (idA): %d\n", idA)
    fmt.Printf("Alice ID key (ikpA.Priv): %x\n", *ikpA.Priv)
    fmt.Printf("Alice ID key (ikpA.Pub): %x\n", *ikpA.Pub)
    fmt.Printf("Alice Pre-key (spkA.Priv): %x\n", *spkA.Priv)
    fmt.Printf("Alice Pre-key (spkA.Pub): %x\n\n", *spkA.Pub)

    fmt.Printf("Bob ID (idB): %d\n", idB)
    fmt.Printf("Bob ID key (ikpA.Priv): %x\n", *ikpB.Priv)
    fmt.Printf("Bob ID key (ikpA.Pub): %x\n", *ikpB.Pub)
    fmt.Printf("Bob Pre-key (spkA.Priv): %x\n", *spkB.Priv)
    fmt.Printf("Bob Pre-key (spkA.Pub): %x\n\n", *spkB.Pub)


    fmt.Printf("== Ephermal keys\n")
    ekA := signal.GenerateEphemeralKeyPair()

    fmt.Printf("Alice Ephemeral key (ekA.Priv): %x\n", *ekA.Priv)
    fmt.Printf("Alice Ephemeral key (ekA.Pub): %x\n", *ekA.Pub)


    // Calculate DH parameters and keys

    dh1 := signal.DH(ikpA.Priv, spkB.Pub)
    dh2 := signal.DH(ekA.Priv, ikpB.Pub)
    dh3 := signal.DH(ekA.Priv, spkB.Pub)


    fmt.Printf("\n== Alice calculates\n")

    fmt.Printf("DH1: %x\n", *dh1)
    fmt.Printf("DH2: %x\n", *dh2)
    fmt.Printf("DH3: %x\n", *dh3)

    dhList := [][]byte{dh1[:], dh2[:], dh3[:]}

    res := signal.KDF(dhList...)

    fmt.Printf("\nKey (RootKey, ChainKey, Index): %x\n\n", *res)


    dh1 = signal.DH(spkB.Priv, ikpA.Pub)
    dh2 = signal.DH(ikpB.Priv, ekA.Pub)
    dh3 = signal.DH(spkB.Priv, ekA.Pub)

    fmt.Printf("== Bob calculates\n")

    fmt.Printf("DH1: %x\n", *dh1)
    fmt.Printf("DH2: %x\n", *dh2)
    fmt.Printf("DH3: %x\n", *dh3)

    dhList = [][]byte{dh1[:], dh2[:], dh3[:]}

    res = signal.KDF(dhList...)

    fmt.Printf("\nKey (RootKey, ChainKey, Index): %x\n", *res)
 
}