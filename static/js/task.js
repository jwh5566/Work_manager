/**
 * Created by Administrator on 2017/12/13.
 */
function task_delete(id, url) {
    $.ajax({
		type: "POST",
		url: url,
		data: {task: id},
		dataType: "json",
		success:task_delete_confirm,
		error: function(){
            alert('Error1')
		}
	});
}

function task_delete_confirm(response) {
    task_id = JSON.parse(response);
    if (task_id>0) {
        $('#task_' +task_id).remove();
    }
    else {
        alert('Error2');
    }
}