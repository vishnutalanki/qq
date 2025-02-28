namespace DeutschAlgorithm {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    // Oracle for a BALANCED function: f(x) = x
    operation BalancedOracle(inputQubit: Qubit, ancillaQubit: Qubit) : Unit {
        CNOT(inputQubit, ancillaQubit); // If input=1, flip ancilla
    }

    // Oracle for a CONSTANT function: f(x) = 0
    operation ConstantOracle(inputQubit: Qubit, ancillaQubit: Qubit) : Unit {
        // Do nothing (ancilla remains |0⟩)
    }

    operation RunDeutschAlgorithm(oracle: ((Qubit, Qubit) => Unit)) : Result {
        use (inputQubit, ancillaQubit) = (Qubit(), Qubit());
        X(ancillaQubit); // Prepare ancilla in |1⟩
        ApplyToEach(H, [inputQubit, ancillaQubit]); // Superposition
        oracle(inputQubit, ancillaQubit); // Query oracle
        H(inputQubit); // Interference
        return MResetZ(inputQubit); // Measure
    }
}