---
layout: post
title: About easy to implement visual impairment accessibility features.
tags: Accesibility WIP
---

{% assign media = site.baseurl | append: "assets/media/" | append:  page.path | replace: ".md","" | replace: "_posts/",""  %}


!!! attention
    Work In progress

Imagine: today is the release date of the game you have been waiting during months. Call it Star Citizen, Cyberpunk 2077 or the steam version of Dwarf Fortress. You spend a nice amount of money, download it and start it. Once inside the game you can’t understand the main menu. That’s not a problem, you just guess and manage to start a game. Sencond disapointment: you can’t see the in-game interface. The game is unplayable. It looks interesting, you devise some of the features shown in the trailer, but you can’t play it. It is torture.

This is an empathy exercise about what people with visual impairment feels with a lot of games. Hopefully, most of the people reading this will not have this problem. Vision related disabilities have a huge impact on the daily people's lifes, the least we can do as a game developers is to allow them to enjoy our games. At the end that's the goal of game developers, to create something for others to enjoy.

This report from the WHO (World Health Organization) about [Blindness and vision impairment](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment) tells us that 2.2 billion people have a near or distance vision impairment. For reference, at the time writting this there are 7.7 billion people living on earth, that means that 28% of the global population has some kind of visual condition. Thankfully most of those cases are mild, so we will need to dig a bit deeper to find the number of people with moderate and severe vision impairment.

The report about [global data on visual impairments 2010](https://www.who.int/blindness/GLOBALDATAFINALforweb.pdf) made by the WHO shows us this table:

| Ages (in years) | Population (millions) | Blind (millions) | Low Vision (millions) | Visually Impaired (millions) |
|:---------------:|:---------------------:|:----------------:|:---------------------:|:----------------------------:|
| 0-14            | 1,848.50              | 1.421            | 17.518                | 18.939                       |
| 15-49           | 3548.2                | 5.784            | 74.463                | 80.248                       |
| 50-inf          | 1,340.80              | 32.16            | 154.043               | 186.203                      |
| **all ages**    | **6,737.50**          | **39.365**       | **246.024**           | **285.389**                  |

That means that 4.24% of the global population is visually impaired (0.58% blind and 3.65% low vision). Those numbers make more sense, although we still have to take them with a grain of salt for various reasons, the most important being that the tests do not take into account the colour blindness. This data should give us an idea of how many people will experience visual problems when playing or games.

But don't worry, there is a way to allow visually impaired people to play our games: accesible design. During the presentation 	[Accessible Player Experiences: A New Approach to Data Informed Design for Accessible Games](https://www.youtube.com/watch?v=pa6fsPMqAmU) done by the [The AbleGamers Charity](https://ablegamers.org/) in the 2019 [Game Developers Conference](https://gdconf.com/), they described accesibility with these words:

>Accesibility in games is about getting players having experiences in games alongside their peers.

A more technical definition from [The Web Accesibility Initiative](https://www.w3.org/WAI/), an initiative from the [World Wide Web Consortium](https://www.w3.org/), defines it as:

> Web accessibility means that websites, tools, and technologies are designed and developed so that people with disabilities can use them.

I think you get the idea. So the question now is: How do I make my game accesible? That question is tricky because it is really complicated to make a game 100% accesible for everybody. The conditions of our players can vary a lot and covering all of them can be a huge challenge. We, as indie developers, might not have the resources or experience of AAA game companies, but that's not an excuse to not to provide some basic accesibility features. 

In this post my goal is to cover two topics that will make our game way more accesible for the visually impared people and that are really easy to implement. That's the key point, easy. Low effort, big gains. At the end I also will talk about other interesting accesibility topics.

### GUI scaling

This is probably the most important accesibility feature. The hability to scale the GUI (Graphical User Interface) tries to make it easier for the people with [low vision](https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/low-vision).  It is based on a really complex principle: the bigger the easier to see. Seems easy right? You just need to make everything bigger and thats all. If you have designed interfaces for games before I am sure you know that what might seem easy on the surface, ends up being really complicated. This post is not about GUI design but I will leave you at the end some interesting posts about the importance of this topic since usually it is overlooked.

To continue the explanation it is needed to understand the different kinds of user interfaces in games. The most comon clasification is this one:

![Diagram about the diferent kinds of game interfaces extracted from A sound idea: An investigation into accessible video game design for the deaf and hard of hearing]({{ media }}/kinds_of_interfaces.png)
*Diagram about the diferent kinds of game interfaces extracted from [A sound idea: An investigation into accessible video game design for the deaf and hard of hearing](https://www.researchgate.net/publication/319174070_A_sound_idea_An_investigation_into_accessible_video_game_design_for_the_deaf_and_hard_of_hearing).*

For the sake of this post we are just going to clasify them in two:

- **Non-diegetic**: Does not belong to the fictional world. It is just seen by the players in the real world.

- **Diegetic**: Belongs to the game world. Can be percived by the characters.

When making our game interface scalable we should allow to scale the diegetic and non-diegetic elements independendly. Just in case you are not following me: the user should be able to make zoom and scale the buttons without one thing afecting the other, it is not about changing the render resolution. This is useful not just for accesibility purposes but also to be able to adapt our interface to diferent display sizes and [DPI](https://en.wikipedia.org/wiki/Dots_per_inch)s. I will add another suggestion: allow the text to be scaled independently of the non-diegetic interface (buttons, menus, subtitles etc.). Depending on our design choices the buttons and icons might be recognizable enough but not the text.

So far seems easy right? Believe me, you will have problems. Two elements will collide, the text will get outisde its box, some elements will look ginormous etc.

![Wireframe sketch with problems.]({{ media }}/sketch_problems.png)
*Wireframe sketch with problems.*

It is a good idea to start thinking your interface with these decision in mind. Having these problems means that the interface was not designed properly, and that, besides the accesibility, probably it will not look right in all screen sizes and resolutions. If you archive to make an implementation with these points you will have moved a big step towards accesibility and good design.

### Colours

Sometimes baking things bigger is not enough. Some people suffers from colour blindness. The bare minimum is to provide at least two palettes: one for aesthetical reasons and another one with high contrast. A high contrast palette will help both, people wit low vision and colour blindness. But sometimes this might not be enough. We will start talking about high contrast.

How much contrast is enough? That is an easy one, 7:1 contrast ratio is enough for most use cases. Let me explain. Any colour (inside a colour space) has what is called [relative luminance](https://en.wikipedia.org/wiki/Relative_luminance). Having the relative luminance of two colours we can calculate the contrast ratio with this formula:

$$ CR = \frac{L1 + 0.05}{L2 + 0.05} $$

Where L1 is the relative luminance of the lighter colour and L2 the relative luminance of the darker colour. In order to calculate the relative luminance we use this formula:

$${\displaystyle Y=0.2126R+0.7152G+0.0722B.}$$

But wait, usually we work with gamma-compressed RGB, so first, we have to decompress the RGB values to gamma-expanded values. We can use this easy to remember formula for that:

$$ {\displaystyle \gamma ^{-1}(u)={\begin{cases}{\frac {u}{12.92}}&={\frac {25u}{323}}&u\leq 0.04045 \newline \left({\tfrac {u+0.055}{1.055}}\right)^{2.4}&=\left({\tfrac {200u+11}{211}}\right)^{\frac {12}{5}}&{\text{otherwise}}\end{cases}}}$$

Where $u$ is ${R_{\mathrm {srgb} }}$, ${G_{\mathrm {srgb} }}$, or ${B_{\mathrm {srgb} }}$.

**There must be an easier way...** Yes, there is the [WebAIM](https://webaim.org/resources/contrastchecker/) website, that calculates all of this automatically and gives us examples of how different text sizes would look with those colours. If you are working with web technologies I recomend you to use the [Stark](https://www.getstark.co/) google chrome extension. It allows you to select text inside a web and it will calculate everything for you. It also allows you to simulate vision problems on the whole website.

Okay, so now we know how to calculate the contrast, but how much is enough contrast? The [Web Accesibility Initiative](https://www.w3.org/WAI/) stipulates how much is the minimum and the enhanced color contrast in their [reference document](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0&col_overview#contrast-minimum). Take into account that this is thought for web development, but these numbers also should work fine for videogames.

|                 | AA (minimum) | AAA (enhanced) |
|-----------------|:------------:|:--------------:|
| **Normal text** | 4.5:1        | 7:1            |
| **Large text**  | 3:1          | 4.5:1          |

We should aim for the AAA. Here there are a few test that I have done. The background always is the same, but the content changes to archive the desired contrast ratio.

![Test showing multiple contrast ratios.]({{ media }}/contrast_test.png)
*Test showing multiple contrast ratios.*

That does not mean that we have to create a palette where every color has a contrast ratio of 7:1 with all the other colours. We have to think about how are we going to use those colours and just worry about the contrast of elements that give information. Quoting the Web Accesibility Initiative about incidental text:

> Text or images of text that are part of an inactive user interface component, that are pure decoration, that are not visible to anyone, or that are part of a picture that contains significant other visual content, have no contrast requirement.

That means that we should not worry about the colours whose only purpose is to be used for decorations. But be careful, elements different from text that give some kind of information also deserve high contrast, for example, the lines that organize our UI. Here is an example:

![Example showing where to use high contrast colours.]({{ media }}/ui_test.png)
*Example showing where to use high contrast colours.*

Just one color, used in the vertical separators, has changed. In the first example we see how the shadows are lost, but all the important information still is there. On the second example the vertical separators disapear. This information is not trivial, so we should avoid designs like this one. Also, it looks like crap.

As I said, a high contrast palette might not be enough. This is specially true when colours are meaningful inside a game. For example colours of teams. In these kinds of situations is hard to design with high contrast. What if there are 5, or even more, teams? Should each one have a different luminance?  Thankfully these situations are not a problem for people with low vision problems. As far as there is enough contrast between the players and the background they will be able to see properly the shapes. But what for colour blind people? Let's see an example:


![Example showing two teams, green and red, over brown background. Second image with deuteronopia filter.]({{ media }}/teams_test2.png)
*Example showing two teams, green and red, over brown background.Second image with deuteronopia filter.*

As you can see in thes image

### Resources

- [Level Up – A Guide to Game UI (with Infographic)](https://www.toptal.com/designers/gui/game-ui): nice explanation about the different kinds of game UI.

- [Games for change student challenge: game accesibility resources](http://gamesforchange.org/studentchallenge/game-accessibility-resources/): this website has a ton of resources to make our games more accesible.

- [Able Gamers Charity](https://ablegamers.org/): charity whose mision is making games more accesible.

- [sRGB, RGB & Gamma](https://observablehq.com/@sebastien/srgb-rgb-gamma): a technical, well made, interactive, and easy to understand guide about colour properties. It has a chapter about accesibility and colour blindness simulation.

- [The Science of Color Contrast — An Expert Designer’s Guide](https://medium.muz.li/the-science-of-color-contrast-an-expert-designers-guide-33e84c41d156): a concise guide about colour contrast.

- [How to Meet WCAG (Quick Reference)](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0&showtechniques=141%2C146&currentsidebar=%23col_overview#contrast-enhanced): reference made by the Web Accesibility Initiative.

- [jsColorblindSimulator](http://mapeper.github.io/jsColorblindSimulator/): the best color blind simulator for images I have found. Here it is the [github repo](https://github.com/MaPePeR/jsColorblindSimulator). Only thing missing is the option to download images.