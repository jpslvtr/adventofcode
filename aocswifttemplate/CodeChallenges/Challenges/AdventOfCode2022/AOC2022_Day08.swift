import ChallengeBase

extension AoC2022 {
    class Day08 : AoC2022, Solution {
        // MARK: - Type Aliases
        typealias Input = [Command]
        typealias Output = Int
        
        
        // MARK: - Properties
        var testCases: [TestCase<Input, Output>] = []
        var selectedResourceSets: [String] = []
        var selectedAlgorithms: [Algorithms] = []
        
        
        // MARK: - Initializers
        init(datasets: [String] = [], algorithms: [Algorithms] = []) {
            self.selectedResourceSets = datasets
            self.selectedAlgorithms = algorithms
        }
        
        
        // MARK: - Solution Methods
        // Step 1: Assemble
        func assemble(_ rawInput: String, _ rawOutput: String? = nil) -> (Input, Output?) {
            let formattedInput: [Command] = rawInput.replacingOccurrences(of: "$", with: "~\n$")
                .components(separatedBy: "~")
                .filter { !$0.isEmpty }
                .compactMap { segment in
                    var lines: [String] = segment.components(separatedBy: .newlines)
                        .filter { !$0.isEmpty }
                                                            
                    return (command: lines.removeFirst(), output: lines)
                }
            
            let formattedOutput = rawOutput?.integerList()[0]
            
            return (formattedInput, formattedOutput)
        }
        
        // Step 2: Activate
        func activate(_ input: Input, algorithm: Algorithms) -> Output {
            switch algorithm {
            case .part01:
                return part01(input)
            case .part02:
                return part02(input)
            }
        }
        
        
        // MARK: - Logic Methods
        func part01(_ inputData: Input) -> Output {
            // blah
        }
        
        func part02(_ inputData: Input) -> Output {
            // blah
        }
        
        
        // MARK: - Helper Methods
  
    }
}
