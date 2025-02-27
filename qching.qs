namespace Quantum.Demo {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Measurement;

    @EntryPoint()
    operation CoinFlipSumSixTimes() : Int[] {
        mutable allResults = [];
        for _ in 1..6 {
            mutable sum = 0;
            for _ in 1..3 {
                use qubit = Qubit();
                H(qubit); // Apply Hadamard gate to create superposition
                let result = M(qubit); // Measure the qubit
                Reset(qubit); // Reset the qubit before releasing
                set sum += if result == Zero { 2 } else { 3 };
            }
            set allResults += [sum];
        }
        return allResults;
    }
}