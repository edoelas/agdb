---
layout: post
title: A story about pixel art colour processing
tags: Image pixel-art 
---

{% assign media = site.baseurl | append: "assets/media/" | append:  page.path | replace: ".md","" | replace: "_posts/",""  %}


- Todos los subaparados deben desaparecer
- Plantear problema y preguntas al principio
- Contar una historia


Taiwan, 23 May 2020:

I need to finish the script today. Bla bla bla


### The problem

I have rendered some pixel art images, but the colours are not smooth. They might seem to the human eye, but they are not. I also need to swap their palette for a different one.

### The first approach

I discovered, after a lot of try and error, that not smoothing the image colours befor I swap the palette will make that some pixels look out of place. That's the reason why I decide to split the processing in two parts:
1. Reducing the colours
2. Swaping the palette

```python
def reduce_colors(img, threshold):
    colors = list()
    # Iterate through all the pixels
    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            dist = float("inf")
            index = 0
            # Iterate over the colours calculating the minimal distance
            for pos, color in enumerate(colors):
                new_dist = np.linalg.norm(color-pixel)
                if new_dist < dist:
                    dist = new_dist
                    index = pos
            # If the colour difference is smaller than the threshold
            # swap the colour for the closest one
            if dist < threshold:
                img[y][x] = colors[index]
            # Otherwise, add the colour to the list of colours
            else:
                colors.append(pixel)

    return img


def swap_colours(img, palette):
    palette = palette.reshape(-1,4)
	# Iterate through all the pixels
    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            dist = float("inf")
            index = 0
            for pos, color in enumerate(palette):
                new_dist = np.linalg.norm(color-pixel)
                if new_dist < dist:
                    dist = new_dist
                    index = pos

            # If is not 100% transparent swap the colour
            if(pixel[3] != 0):
                img[y][x] = palette[index]

    return img
```




### The good approach

This approach is garbage:
- Too slow. Does not take proffit from the matrix capabilities of numpy.
- Just consider the first colour
- We don't know the ammount of resoulting colours

New idea:
- Get the reduced colour palette instead of the image
- remap the image colours with the new palette

Of course, for this new idea to be better we will have to change how our functions work.

Let's start with the reduced palette. If we have a group of points in a 3D space arranged in clusters, maybe, and just maybe, a clustering algorithm is the right choice. But there are many. To know which one is the adequate one a good place to start is the [Clustering from Scikit Learn](https://scikit-learn.org/stable/modules/clustering.html#clustering). 

![Overview of clustering methods.]({{media}}/clustering_algorithms.png)
### The benchmark