import ChallengeBase

// MARK: - Challenge Algorithms
enum AoC2022_Algorithms : String, CaseIterable {
    case part01
    case part02
}


// MARK: - Challenge Class
class AoC2022 : Challenge {
    // MARK: - Type Aliases
    typealias Algorithms = AoC2022_Algorithms
        
    
    // MARK: - Computed Properties
    var baseResourcePath: String {
        get {
            return #file
                .replacing(#"/Challenges/"#, with: "/Resources/")
                .replacing("/\(self.name).swift", with: "")
        }
    }
    
    var name: String {
        get { return String(String(describing: self).split(separator: ".")[1]) }
    }
}
