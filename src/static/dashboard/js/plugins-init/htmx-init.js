document.addEventListener("DOMContentLoaded", function () {
    // code...

    htmx.onLoad(function (content) {
        var sortables = content.querySelectorAll(".sortable");
        for (var i = 0; i < sortables.length; i++) {
            var sortable = sortables[i];
            var sortableInstance = new Sortable(sortable, {
                animation: 150,
                ghostClass: 'blue-background-class',

                // Make the `.htmx-indicator` unsortable
                filter: ".htmx-indicator",
                onMove: function (evt) {
                    return evt.related.className.indexOf('htmx-indicator') === -1;
                },

                // Disable sorting on the `end` event
                onEnd: function (evt) {
                    this.option("disabled", true);
                }
            });

            // Re-enable sorting on the `htmx:afterSwap` event
            sortable.addEventListener("htmx:afterSwap", function () {
                sortableInstance.option("disabled", false);
            });
        }
    })

    var listItems = [1, 2, 3, 4, 5]
    // routes
    // init("/demo", function (request, params) {
    //     return '<form id="example1" class="list-group col sortable" hx-post="/items" hx-trigger="end">' +
    //         listContents() +
    //         "\n</form>";
    // });

    // onPost("#", function (request, params) {
    //     console.log(params);
    //     listItems = params.item;
    //     return listContents();
    // });

    // templates
    function listContents() {
        return '<div class="htmx-indicator" style="cursor: default">Updating...</div>' + listItems.map(function (val) {
            return `  <div style="border:1px solid #DEDEDE; padding:12px; margin: 8px; width:200px; cursor: grab" ondrag="this.style.cursor = 'grabbing'" ><input type="hidden" name="item" value="` + val + `"/> Item ` + val + `</div>`;
        }).join("\n");
    }

});