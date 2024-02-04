document.addEventListener("DOMContentLoaded", () => {
	let introduction = '"Taha Yaseen, Senior Python/Django Dev';
	animateTyping(introduction, "introduction", 50);
});

function animateTyping(text, elementId, animationSpeed) {
	let element = document.getElementById(elementId);
	let animatedText = "";

	let charPos = 0;
	function animate() {
		if (charPos < text.length) {
			animatedText += text.charAt(charPos);
			element.innerText = animatedText + "|";
			charPos++;
			setTimeout(animate, animationSpeed);
		} else {
		}
	}

	animate();
}
