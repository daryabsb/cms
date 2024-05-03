document.addEventListener("DOMContentLoaded", function () {
    // code...

    htmx.onLoad(function (content) {
        console.log("End event triggered");
        var sortables = content.querySelectorAll(".sortable");
        var nestable1 = document.getElementById('nestable');

        "use strict";


        $("#nestable").nestable({
            group: 1,
        }).on("change", e)

        var e = function (e) {
            var t = e.length ? e : $(e.target);
            console.log('#someButton was clicked');
            var structure = $(this).nestable('serialize');
            saveStructure(structure);
        };

        /*******************
        Nestable
        *******************/
        function saveStructure(data) {

            console.log("Menu id from additional = ", menu_id);
            // Send AJAX request to server to save the new structure
            // var menu_id = jQuery(this).attr('rel');
            var form_data = $("#MenuItem" + menu_id + "Form").serializeArray();


            var menu_name = $('#MenuNameEdit').val();

            menu_data.menu_id = menu_id; // Update menu_id in menu_data
            menu_data.menu_name = menu_name; // Update menu_name in menu_data


            var dd_data = JSON.stringify(data); // Serialize Nestable data

            console.log("Menu_id = ", menu_id);
            console.log("Menu_data = ", JSON.stringify(menu_data));
            console.log("Form_data = ", form_data);
            console.log("dd_data = ", dd_data);

            $.ajax({
                headers: {
                    'X-CSRF-TOKEN': CSRF_TOKEN
                },
                url: '/htmx/menu-structure-save/',
                method: 'POST',
                data: {
                    csrfmiddlewaretoken: CSRF_TOKEN,
                    'dd_data': dd_data,
                    'menu_data': menu_data,
                    'form_data': form_data
                },
                success: function (res) {
                    if (res.success) {
                        $('.MenuSelectDiv .nice-select .current').text(menu_name);
                        $('.MenuSelectDiv .nice-select .list .selected').text(menu_name)
                        // alert(res.success);
                        Swal.fire({
                            type: 'success',
                            title: 'Save Successfully',
                            text: 'All Menu Item Save Successfully',
                            confirmButtonColor: "var(--primary)"
                        });
                    }
                    if (res.error) {

                        Swal.fire({
                            type: 'warning',
                            title: 'Not Allow',
                            text: res.error,
                            confirmButtonColor: "var(--primary)"
                        })

                    }
                },
                error: function (xhr, status, error) {
                    console.error('Error saving structure:', error);
                }
            });
        }

        // ,
        //     $("#nestable2").nestable({
        //         group: 1
        //     }).on("change", e), e($("#nestable").data("output", $("#nestable-output"))), e($("#nestable2").data("output", $("#nestable2-output"))), $("#nestable-menu").on("click", function (e) {
        //         var t = $(e.target).data("action");
        //         "expand-all" === t && $(".dd").nestable("expandAll"), "collapse-all" === t && $(".dd").nestable("collapseAll")
        //     }), $("#nestable3").nestable();


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


    // const saveMenuBtn = document.getElementById('SaveMenu');
    // const menuNameInput = document.getElementById('MenuNameEdit');
    // const menuItemForms = document.querySelectorAll('form[id^="MenuItem"]');

    // saveMenuBtn.addEventListener('click', function () {
    //     console.log("SAVE MENU CLICKED");
    //     console.log("CSRF_TOKEN = ", CSRF_TOKEN);
    //     const data = gatherMenuData(menuNameInput, menuItemForms);
    //     sendMenuData(data);
    // });





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

function initializeNestables() {
    var nestable1 = document.getElementById('nestable');
    var nestable2 = document.getElementById('nestable2');
    var nestableOutput1 = document.getElementById('nestable-output');
    var nestableOutput2 = document.getElementById('nestable2-output');

    var nestableConfig = {
        group: 1,
        onChange: function () {
            // Your change event handling logic here
        }
    };

    new Nestable(nestable1, nestableConfig);
    new Nestable(nestable2, nestableConfig);

    nestable1.addEventListener('change', function () {
        // Update output for nestable 1
        nestableOutput1.innerText = JSON.stringify(nestable1.nestable('serialize'));
    });

    nestable2.addEventListener('change', function () {
        // Update output for nestable 2
        nestableOutput2.innerText = JSON.stringify(nestable2.nestable('serialize'));
    });

    document.getElementById('nestable-menu').addEventListener('click', function (event) {
        var action = event.target.dataset.action;
        if (action === 'expand-all') {
            nestable1.nestable('expandAll');
            nestable2.nestable('expandAll');
        } else if (action === 'collapse-all') {
            nestable1.nestable('collapseAll');
            nestable2.nestable('collapseAll');
        }
    });

    var nestable3 = document.getElementById('nestable3');
    new Nestable(nestable3);
}