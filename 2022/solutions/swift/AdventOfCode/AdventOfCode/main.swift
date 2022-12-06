import Foundation

func greet(person: String) -> String {
    let greeting = "Hello, " + person + "!"
    return greeting
}

func readFile(fileName: String) -> Array<String> {
    var res = [String]()
    let contents = try! String(contentsOfFile: fileName, encoding: .utf8)
    res.append(contents)
    return res
}

print(readFile(fileName: "../../../../inputs/5.txt"))
