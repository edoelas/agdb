---
layout: post
title: I am a sinner
tags: ~WIP~ Presentation meta design blog
---

{% assign media = site.baseurl | append: "assets/media/" | append:  page.path | replace: ".md","" | replace: "_posts/",""  %}

I said I wanted to keep this blog as minimal as possible. I bragged about the few lines I use. That I was using just 60 lines of CSS in total. And what have I become? Now I use 70 lines of CSS just for syntax highlighting and another 120 for the rest of the things. How many lines I will be using tomorrow? 10.000? 100.000? Nobody knows. I have becomed what I promissed to destroy. I wanted to destroy the bloat and now I am the bloat. I have become a monster.

Okay, enough stupidity for today, now I am going to talk about what happened. As I said I am not a web designer but as any human I like beautiful things. So what happend? I just woke up one morning and decided to spend my whole day fiddling with CSS? No, first I needed to open my eyes. Two days ago, 23 May 2021, the day of the creation of this blog, at 22:08 I send the blog link to one of my friends and he replies:

> "It is as ugly as hitting a father."<br>- A. K.

It was not imediate but that comment is what started the redesign. The truth is that the default colours and fonts are not the best ones. Maybe by changing that I could make the blog a bit more appealing.

When I did my first blog I loved its home page but two days ago, when I changed the layout of it, I discovered that my old home page was garbage. Twodays ago I thought that the design of my blog was almost perfect. Now I think it was garbage. As we say here: "he who does not know god will pray to any saint." And that is exactly what happened. My question now is: in a year or so, will I find that this blog is garbage and discover something way better? Is that even possible? I would think that is not potssible, but the recent past tells the oposite.

### The changes

Originally I just thought of doing a few quality of life changes. Most of them are already done:

- **Adding RSS**. Yes, you can read my blog withot ever entering my blog. Without appreciating the beauty of it.

- **Hide useless links when printing**. If you want to print some article now you can do it withot printing the ugly [home]({{ site.baseurl }}) links. I don't know if anybody will do that but it is a problem that I have found when wanting to save a webpage as a PDF.

- **Google analytics**. Google knows what are you eating right now. Are you using [DuckDuckGo](https://duckduckgo.com/)? Useless in this page. I just want to know (for free) how many people is visiting my blog and where are the visitors from. Any alternatives are welcome, my email is at the end of the home screen. 

- **Improved the HTML code**. It was quite good, but there were still some problems because I did not understood properly how [Liquid](https://shopify.github.io/liquid/) works. Now it is even better.

There are still some things to do:

- Improve search
- Adapt design for smartphones
- [Solve hassle with image insertion](https://stackoverflow.com/questions/67660810/is-there-a-way-in-jekyll-to-set-a-base-path-for-images)
- Alt text below images

### The redesign

First of all and the most important thing: **No HTML code has been harmed during the redesign of this blog**. The HTML code hasn't been changed at all. Everything is CSS work. That's nice.

Another important thing: **No useless CSS clases have been created to archive this purpose**. All the redesign has been done by modifying the HTML elements. I have just created one class, `.dontprint`, which is used to hide the home links when printing.

How did I make it? By overwritting the classes used by Jekyll when converting my [Markdown](https://en.wikipedia.org/wiki/Markdown) to HTML. Most of the work has been done on the fonts. To get the fonts right (or what seems right to me) seamed really challenging but after reading some guides I think I made good decisions. At the end of the page I will leave some resources I find interesting but now I want to share with you the most influential one: [Choosing Web Fonts: A Beginner’s Guide](https://design.google/library/choosing-web-fonts-beginners-guide/). First, the content is interesting for begginers. Second, don't you see a similarity between that blog and my blog? No, I did not copy everything. When I found this blog post I already knew that I was going to use roboto, that I wanted black letters over white background and some other decisions. To decide the weight and size of the fonts I used another guide. So what did I took from this website? Two important things: the colours and the links.

#### Links

Lets start with the links. CSS allow you to modify the apperance of the links under four different circumstances: unvisited, visited, hovered and, pressed. First I thought about changing the color to a lighter gray when hovering and then to an enven lighter gray when pressing. I also was thinking to let the user know when a link has been already visited... probably using another gray? Four grays just for the links are too many grays. Using two different grays for text is fine. Three for some specific purposes can be interesting but Four for the same element? No. If you have a look to the [Google Design blog](https://design.google/library/racial-equity-everyday-products/) they use black for links and on hover they hide the underline. Just beautiful. It is not intrusive, does not require to use more colours, is easy to understand and to implement, gives exactly the right amount of information, it blends really well with the rest of the text etc. I like to use lots of links insde the text and this is a perfect solution. The CSS code looks like this:

```css
a{ color: var(--black);}
a:hover, a:active {text-decoration: none;}
```

#### Colours

Now we are going to talk about the colour. In lots of websites I have seen backgrounds and letters that ar gray. Dark gray letters on top of light gray background. I believed in this choice since the contrast was reduced, making it les uncomfortable to look at, while the text could be read perfectly. But the designers in google are really brave. Black on top of white. In that post the letters are gray but in the most recent ones they are using black letters. In the material design guide about [Text legibility](https://material.io/design/color/text-legibility.html#legibility-standards) they also suggest to use dark gray for less importante content. Finally I also have used a light gray to use it as a box for special content, for exmaple, with code blocks:

```python
def factorial(x):
    if x == 1: return 1
    else: return (x * factorial(x-1))
```
 Now I have 4 colours, `#fff`, `#eee`, `#333`, `#000`, each one with a specific purpose. That's all I need. I find it really comfortable to read while keeping a contrast high enough that everybody can read it.

![Colours in order: #fff, #eee, #333, #000]({{ media }}/colours.png)

Another question to think about is which color palette use for the code highlight. I think that is something I will take care in the future. So far I have just choosen the [Tango](http://jwarby.github.io/jekyll-pygments-themes/languages/python.html) theme from [Pygments](https://pygments.org/) but I will modify it soon since I have been told that the bright green and orange might not have enough contrast.

#### Fonts
As I said I wanted to use Roboto as the font for my text. It is used by google so it must be a good choice. I think the google designers know a couple of things about web design. I was planning to use a secondary font for some specific purposes but looking at the google design blog I found out that they were using only (that's not 100% true) Roboto. In the guide about [the type system](https://material.io/design/typography/the-type-system.html#applying-the-type-scale) I discovered that it was not just about using one or two diffrent fonts and call it a day. It was about choosing the right size, weight, colour and spacing. So once again I believed in Google and used only Roboto. In fact, for the inline code and code blocks I am using Roboto in its mono variant. I am happy the fonts are looking now but there is room for improvement. I have barely touched the spacing between lines, words and characters.

### Conclusion

I have done more things than the ones I have explained here but this is not about web development. My thinking when writting this blog is that I could help other developers who decide to create their own blog. At the end I am using just 90 extra CSS lines and importing 2 fonts. I am not a designer by any mean, in fact, as you may have discovered basically I just have merged some things that I found interesting. If you are curious about the CSS it is published on github under the path `/assets/css/BMFB.css`. The name stands for Better Mother Fu**ng Blog as a tribute to [bettermotherfuckingwebsite](http://bettermotherfuckingwebsite.com/), web that I used as my main inspiration when doing the first version of the Blog.

Probably there is one last post about the blog itself where I will talk about the supersimple search engine that I will implement and some minor changes. There are also some markdown elements that I haven't shown yet. Those elements are latex-like math formulas:

$$mean = \frac{\displaystyle\sum_{i=1}^{n} x_{i}}{n}$$

and tables:

| First name      |Last name| Number|
| :------------- | :----------: | -----------: |
|  Mario | Vargas   | 123123123    |
| Manuel   | Goterris | 13058375 |
| Pablo   | Albiol | 247674363 |

Here there are some resources that I find interesting:


[Material design: Text legibility](https://material.io/design/color/text-legibility.html#legibility-standards)

[Material design: The type system](https://material.io/design/typography/the-type-system.html#applying-the-type-scale)