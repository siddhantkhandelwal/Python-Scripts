var tableWrapper = function(code, className=null){
    return "<table class=" + className + ">" + code + "</table>"
}
var tableBodyWrapper = function(code, className=null){
    return "<tbody class=" + className + ">" + code + "</tbody>"
}
var row = function(className=null, num, item){
    return ("<tr class="+className+"><td>"+num+
            "</td><td>"+item+"</td>"+"<td><input type='checkbox'"+
            "onclick='myFunction()'></input></td></tr>")
}
var tableHead = function(className=null, item){
    return "<thead><tr><th>No</th><th class="+
            className+">"+item+
            "</th><th>Done</th></tr></thead>"
}
var finalCode = ""
var finalRowCode = ""
console.log(3)
$.getJSON("tasks.json", function(ajson) {
    tasks = ajson.tasks;
    console.log(tasks);
    for(dates in tasks){
        finalCode = tableHead(null,"Tasks")
        var num = 0
        for (entry in tasks[dates]){
            num+=1
            finalRowCode += row(null,num,entry)
        }
        finalRowCode = tableBodyWrapper(finalRowCode,"'demo-table6'")
        finalCode = finalCode + finalRowCode
        finalCode = tableWrapper(finalCode)
        document.write(finalCode)
    }
});