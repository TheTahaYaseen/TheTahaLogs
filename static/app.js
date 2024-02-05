document.addEventListener("DOMContentLoaded", () => {
	let introduction_heading = "Taha Yaseen, Senior Python/Django Dev";
	let introduction_subtitle = "- Enthusiast focused on delivering value";
	let introduction =
		"I'm Taha Yaseen, a passionate coder who began at seven. Specializing in Python and Django, I turn complex challenges into innovative solutions. My journey from hackathons to freelancing has taught me to find opportunity in chaos. I aim to blend coding with change, pushing technology forward. Each project is a chance to inspire and make an impact, fueling my drive to shape the future of tech and empower upcoming developers. I thrive on mentoring and sharing knowledge, believing that every line of code can pave the way for groundbreaking advancements.";
	let animationSpeed = 40;
	let introductionAnimationSpeed = 10;
	animateTyping(introduction_heading, "introduction_heading", animationSpeed);

	let delayForSecondAnimation =
		(introduction_heading.length + 5) * animationSpeed;
	let delayForThirdAnimation =
		(introduction_subtitle.length + 12) * animationSpeed;
	delayForThirdAnimation += delayForSecondAnimation;

	setTimeout(() => {
		animateTyping(
			introduction_subtitle,
			"introduction_subtitle",
			animationSpeed
		);
	}, delayForSecondAnimation);

	setTimeout(() => {
		animateTyping(introduction, "introduction", introductionAnimationSpeed);
	}, delayForThirdAnimation);
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
			setTimeout(() => {
				element.innerText = animatedText;
			}, animationSpeed);
		}
	}

	animate();
}
