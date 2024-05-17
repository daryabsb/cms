var str = '';
function displayData(ch) {
  if (ch == 'C') {
    str = '';
  } else if (ch == '=') {
    var t = str.length;
    for (n = t; n > 0; n--) {
      if (str.substr(-1) == '+' || str.substr(-1) == '-' || str.substr(-1) == '*' || str.substr(-1) == '/') {
        var k = str.length - 1;
        str = str.substr(0, k);
      }
    }
    str = eval(str);
  } else {
    if (str == '') {
      if (ch == '+' || ch == '*' || ch == '/') {
        return Error;
      } else if (ch == '-') {
        str = '-';
      } else {
        str = JSON.stringify(ch);
      }
    } else {
      str = str + ch;
    }
  }
  document.getElementById("message").innerHTML = str;
}