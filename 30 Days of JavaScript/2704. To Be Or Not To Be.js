function expect(val) {
    const origVal = val
    return {
        toBe: function(newVal) {
            if (newVal !== origVal) {
                throw new Error("Not Equal")
            } else return true },
        notToBe: function(newVal) {
            if (newVal === origVal) {
                throw new Error("Equal")
            } else return true
        }
    }
    
}
