var conf = {
  server: "ec2-3-136-116-6.us-east-2.compute.amazonaws.com:3000/",

  path_reserve: "/reserve",
  path_open: "/open",
  path_close: "/close",
}
// server의 주소 (function 별로)

function callPost(data)
{
  $.post(conf.server + conf.path_reserve, data, function(r){
     //var o = JSON.parse(r);
     console.log(r);
     console.log(r.msg);
  });
}
// http post -> reserve 요청

function callPost_open(data)
{
  $.post(conf.server + conf.path_open, data, function(r){
     //var o = JSON.parse(r);
     console.log(r);
     console.log(r.msg);
  });
}
// http post -> open 요청

function callPost_close(data)
{
  $.post(conf.server conf.path_close, data, function(r){
     //var o = JSON.parse(r);
     console.log(r);
     console.log(r.msg);
  });
}
// http post -> close 요청