

document.querySelector("#start-programm").onclick = async (e) => {
	console.log("=)")
	let number = parseInt(document.querySelector("#number-js").value);
	let result = await eel.start_proc_number_py(number)();
    show_result(result);
}


function show_result(dict_result){
    document.querySelector("#result-java").value = dict_result["java"];
    document.querySelector("#result-c").value = dict_result["c"];
    document.querySelector("#result-csharp").value = dict_result["c#"];
    document.querySelector("#result-js").value = dict_result["js"];
    document.querySelector("#result-python").value = dict_result["python"].join(', ');
}

eel.expose(solve_example);
function solve_example(list_of_numbers, x) {
	let sum = 0;
	let part = 0;
	for (let i in list_of_numbers) {
		part = list_of_numbers[i] * ((-1)**(i%3)) * (x**((-1)**i))
		sum += part;
	}
	return (sum).toFixed(3);
}