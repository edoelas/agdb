var idx = lunr(function () {
    this.ref('url')
    this.field('title')
    this.field('tags')
    this.field('date')

    window.documents.forEach(function (doc) {
        this.add(doc)
    }, this)
})

function search() {
    query = document.getElementById("myInput").value;
    results = idx.search(query)

    const results_set = new Set()
    for (const key in results) {
        results_set.add(results[key].ref)
    }

    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    for(let i = 0;i < li.length; i++)
    {
        if ( results_set.has(li[i].id)) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

