var util = require('../lib/util');
var exec = require('child_process').exec;

getRemoteOriginUrl();

function getRemoteOriginUrl(){
  var remoteExecCmd = 'git remote -v';
  var getRemoteExec = exec(remoteExecCmd);
  util.procExec(getRemoteExec, function(res){
    console.log(res);
  });
}