// Sample JavaScript file for testing
 
function calculateTotal(price, quantity) {
    return price * quantity;
}
 
const product = {
    id: 1001,
    name: "Laptop",
    category: "Electronics"
};
 
const total = calculateTotal(250, 3);
 
console.log("Product:", product.name);
console.log("Total:", total);
 
const users = ["Alice", "Bob", "Charlie"];
 
users.forEach(user => {
    console.log(`Welcome ${user}`);
});