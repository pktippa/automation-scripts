function procExec(prexec , callback){
  var rData = "";
  prexec.stdout.on('data', function(data){
    rData += data;
  });
  prexec.stderr.on('data', function(data){
    rData += data;
  });
  prexec.on('close', function(code){
    callback(rData.trim());
  });
}

module.exports = {
  procExec: procExec
}