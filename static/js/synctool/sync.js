let btnRun = document.querySelector("#btn-run");
let modelChecks = document.getElementsByName("check-model");
let taskChecks = document.getElementsByName("check-task");

btnRun.onclick = RunProcess;

let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
let processResult = document.querySelector("#process-result");
let dbEngineBasePath = domain + "/dbengine/";

processResult.value += 'Hello!\n';

function ClearSelection(){
    modelChecks.forEach(m =>{
        m.checked = false;
    });
    taskChecks.forEach(t =>{
        t.checked = false;
    });
}

function SetStatus4All(status=true){
    modelChecks.forEach(m =>{
        m.checked = status;
    });
    taskChecks.forEach(t =>{
        t.checked = status;
    });
}

function RunProcess(){
    
    models = tasks = [];
    modelChecks.forEach(m =>{
        if(m.checked)
           models.push(m.value);
    })
    // SubmitProcess({"models": models});
    ProcessTasks();
    
}

function SubmitProcess(data){
    let props = {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrfToken,
            "Authorization": "Bearer " + authToken
        },
        body: JSON.stringify(data),
        credentials: 'include'
    }

    APIurl = dbEngineBasePath + "sync/local/geodb";
    console.log(APIurl);

    processResult.value += '[Start] -> ' + new Date().toLocaleDateString() + ' ' +  new Date().toLocaleTimeString() + '\n';

    fetch(APIurl, props)
    .then(async response => ({
        result: await response.json(),
        response: response
    }))
    .then(data => {
        processResult.value += '\n['+ data["response"]["status"] + "] - " + data["response"]["statusText"] + ' -> ' + new Date().toLocaleDateString() + ' ' +  new Date().toLocaleTimeString() +'\nResult:\n' + JSON.stringify(data["result"]) + '\n';
    })
    .catch((error) => {
        processResult.value += '\n'+ error['detail'] + '\n';
    });     
}


const ProcessTask = (code, path) => {

    return new Promise((resolve, reject) => {

        let props = {
            method: 'GET',
            headers: {
                "X-CSRFToken": csrfToken,
                "Authorization": "Bearer " + authToken
            }
        }
    
        APIurl = dbEngineBasePath + path;

        processResult.value += '\n[Start] ' + code +': starting @ ' + new Date().toLocaleDateString() + ' ' +  new Date().toLocaleTimeString() + '\n';
        processResult.value += 'running... \n';

        fetch(APIurl, props)
        .then(async response => ({
            result: await response.json(),
            response: response
        }))
        .then(data => {
            resolve(data)
            processResult.value += '\n['+ data["response"]["status"] + "] - " + data["response"]["statusText"] + ': finished @ ' + new Date().toLocaleDateString() + ' ' +  new Date().toLocaleTimeString() +'\nResult:\n' + JSON.stringify(data["result"]) + '\n';
        })
        .catch((error) => {
            
            processResult.value += '\n'+ error['detail'] + '\n';
        });     
        
    })
}

async function ProcessTasks(){
    
    for await(const t of taskChecks){
        if(t.checked){
            const data = await ProcessTask(t.value, t.dataset.path);
            GoToProcessResultBottom();
        }        
    }
    processResult.value += '\ndone!\n\n';
    GoToProcessResultBottom();
}

function GoToProcessResultBottom(){
    processResult.scrollTop = processResult.scrollHeight;
}

