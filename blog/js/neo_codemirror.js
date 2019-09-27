CodeMirror.colorize = (function() {
    var isBlock = /^(p|li|div|h\\d|pre|blockquote|td)$/;

    function textContent(node, out) {
        if (node.nodeType == 3) return out.push(node.nodeValue);
        for (var ch = node.firstChild; ch; ch = ch.nextSibling) {
            textContent(ch, out);
            if (isBlock.test(node.nodeType)) out.push("\n");
        }
    }

    return function() {
        var collection = document.body.getElementsByTagName("code");

        for (var i = 0; i < collection.length; ++i) {
            var theme = " cm-s-default";
            var node = collection[i];
            var mode = node.getAttribute("data-lang");
            if (!mode) continue;
            if (mode === "cypher") {
                mode = "application/x-cypher-query"
            } else if (mode === "java") {
                mode = "text/x-java";
            } else if (mode === "sql") {
                mode = "text/x-sql";
            }

            var text = [];
            textContent(node, text);
            node.innerHTML = "";
            CodeMirror.runMode(text.join(""), mode, node);

            node.className += theme;
        }
    };
})();
