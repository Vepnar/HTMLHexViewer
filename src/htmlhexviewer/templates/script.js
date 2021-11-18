/**
 * @author https://stackoverflow.com/questions/57803/how-to-convert-decimal-to-hexadecimal-in-javascript#57805
 * @param {Number} d 
 * @param {Number} padding 
 * @returns Integer formatted in hex
 */
function decimalToHex(d, padding) {
    var hex = Number(d).toString(16);
    padding = typeof(padding) === "undefined" || padding === null ? padding = 2 : padding;

    while (hex.length < padding) {
        hex = "0" + hex;
    }
    return hex;
}

/**
 * Find all items with the same index
 * @param {Number} index find all elements with this index
 * @param {Boolean} includeRow to include the address or not
 * @returns List of elements
 */
function getTargetElements(index, includeRow) {
    const dataElement = document.getElementById(`data-${index}`);
    const asciiElement = document.getElementById(`ascii-${index}`);

    if (includeRow) {
        const rowIndex = Math.floor(index / 16) // Why isn't there build-in integer division?
        const rowElement = document.getElementById(`row-${rowIndex}`);
        return [dataElement, asciiElement, rowElement];
    } else return [dataElement, asciiElement];

}

/**
 * Remove the hover effect for the items with the same index.
 * @param {Number} index index of unhovered element
 */
function unHover(index) {
    const elements = getTargetElements(index, true)
    elements.forEach(elem => {
        elem.classList.remove("selected");
    })

    // Restore address
    elements[2].innerText = decimalToHex(Math.floor(index / 16), 8);

}

/**
 * Create hover effect for the items with the same index.
 * @param {Number} index 
 */
function onHover(index) {
    elements = getTargetElements(index, true)
    elements.forEach(elem => {
        elem.classList.add("selected");
    });

    // Set address to the address of the current selected item.
    elements[2].innerText = decimalToHex(index, 8);
}

/**
 * Set a highlight step on the given index.
 * @param {Number} index Element index to highlight.
 */
function onClick(index) {
    const elements = getTargetElements(index, false);
    const firstClassList = elements[0].classList;
    let level = 0;

    // Retrieve highlight level
    if (firstClassList.contains("highlight-1")) {
        level = 1;
    } else if (firstClassList.contains("highlight-2")) {
        level = 2;
    } else if (firstClassList.contains("highlight-3")) {
        level = 3;
    } else if (firstClassList.contains("highlight-4")) {
        level = 4;
    }

    elements.forEach(elem => {
        if (level === 0) {
            elem.classList.add("highlight-1");
        } else if (level === 4) {
            elem.classList.remove("highlight-4");
        } else {
            elem.classList.remove(`highlight-${level}`);
            elem.classList.add(`highlight-${level+1}`);
        }
    })
}