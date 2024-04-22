document.addEventListener("DOMContentLoaded", function () {
    // code...

    htmx.onLoad(function (content) {
        var sortables = content.querySelectorAll(".sortable");
        for (var i = 0; i < sortables.length; i++) {
            var sortable = sortables[i];
            var sortableInstance = new Sortable(sortable, {
                animation: 350,
                ghostClass: 'blue-background-class',

                // Make the `.htmx-indicator` unsortable
                filter: ".htmx-indicator",
                // onMove: function (evt) {
                //     return evt.related.className.indexOf('htmx-indicator') === -1;
                // },

                // Disable sorting on the `end` event
                // onEnd: function (evt) {
                //     this.option("disabled", true);
                // }
            });

            // Re-enable sorting on the `htmx:afterSwap` event
            // sortable.addEventListener("htmx:afterSwap", function () {
            //     sortableInstance.option("disabled", false);
            // });
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


    const saveMenuBtn = document.getElementById('SaveMenu');
    const menuNameInput = document.getElementById('MenuNameEdit');
    const menuItemForms = document.querySelectorAll('form[id^="MenuItem"]');

    saveMenuBtn.addEventListener('click', function () {
        console.log("SAVE MENU CLICKED");
        console.log("CSRF_TOKEN = ", CSRF_TOKEN);
        const data = gatherMenuData(menuNameInput, menuItemForms);
        sendMenuData(data);
    });





});
document
    .querySelector('.MenuSelectbtn')
    .addEventListener('click', function () {
        var id = document.getElementById('MenuSelect').value //$("#MenuSelect option:selected").val();
        console.log("got menu id: ", id)
        if (id != "") { window.location.href = "/dashboard/menus/setup/" + id + "/"; }
    });

function gatherMenuData(menuNameInput, menuItemForms) {

    // const menuId = this.dataset.menuId;  // Assuming you have a data-menu-id attribute on the button 
    const menuData = {
        menu_id: menuId,
        menu_name: menuNameInput.value
    };
    const formData = new FormData();
    menuItemForms.forEach(form => formData.append(...form.elements));
    const ddData = JSON.stringify($('.dd').nestable('toArray')); // Assuming you're using nestable.js
    return { menuData, formData, ddData };
}

function sendMenuData(data) {
    data.formData.append('menu_data', JSON.stringify(data.menuData));
    data.formData.append('dd_data', data.ddData);
    fetch(menu_structure_save_url, {
        method: 'POST',
        headers: {
            'X-CSRF-TOKEN': CSRF_TOKEN
        },
        body: data.formData
    })
        .then(response => response.json())
        .then(data => {
            // Handle response data (success/error)
        })
        .catch(error => {
            console.error('Error sending menu data:', error);
        });
}
