
var createCounter = function(init) {
    let count = init;

    function increment() {
        return ++count;
    }
    function decrement() { 
        return --count;
        
    }
    
    function reset(){
        return count = init;
    }

    return {increment, decrement, reset};
};

