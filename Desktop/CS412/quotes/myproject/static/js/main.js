console.log('This is JS from your home page');

const quotes = [
    "A dropout will beat a genius through hard work.",
    "I am not good at ninjutsu or genjutsu... but I want to prove that hard work can surpass genius!",
    "My motto is to be stronger than yesterday, if I have to I'll be stronger than half a day ago, even a minute ago!",
    "It is now the time to carry through and protect one's own way of ninja.",
    "A hero is not one who never falls. He is the one who gets up, again and again, never losing sight of his dreams.",
    "I’m not sad! I’m not sad at all! I’m just... very frustrated!",
    "The lotus of the Leaf Village blooms twice!",
    "I’m going to prove that even without ninjutsu or genjutsu, I can still become a great ninja!",
    "My springtime of youth is not over yet!",
    "If you believe in your dreams, I will prove to you, that you can achieve your dreams just by working hard."
];


const images = [
    "https://static.wikia.nocookie.net/fear-world/images/d/da/Rock_Lee_shippuden.jpg.png/revision/latest?cb=20140904064221",
    "https://wallpapers.com/images/hd/cheerful-rock-lee-thumbs-up-kmwgppbf4wefboxt.jpg",
    "https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/07/rock-lee-is-fighting-in-the-arena.jpg"
];

// Function to get a random index
function getRandomIndex(array) {
    return Math.floor(Math.random() * array.length);
}

// Select a random quote and image
const randomQuoteIndex = getRandomIndex(quotes);
const randomImageIndex = getRandomIndex(images);

// Update the DOM with the selected quote and image
const quoteElement = document.getElementsByClassName('name')[0];
quoteElement.textContent = quotes[randomQuoteIndex];

const imageElement = document.getElementById('quoteImage');
imageElement.src = images[randomImageIndex];
