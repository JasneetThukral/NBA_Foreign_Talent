// removing player from table
//https://www.fourfront.us/blog/store-html-table-data-to-javascript-array/
// var TableData = new Array();
// $('#add_table').each(function(row, tr){
//     TableData[row]={
//         "PlayerID" : $(tr).find('td:eq(0)').text()
//         , "PlayerName" :$(tr).find('td:eq(1)').text()
//         , "Points" : $(tr).find('td:eq(2)').text()
//         , "Assists" : $(tr).find('td:eq(3)').text()
//         ,"Rebounds" : $(tr).find('td:eq(4)').text()
//     }
// });

function addvalues_one() {
    var TableData = new Array();
    $('#add_table').each(function(row,tr){
        TableData[row]={
            "ID" : $(tr).find('td:eq(0)').text()
            ,"PlayerID" : $(tr).find('td:eq(1)').text()
            , "PlayerName" :$(tr).find('td:eq(2)').text()
            , "Points" : $(tr).find('td:eq(3)').text()
            , "Assists" : $(tr).find('td:eq(4)').text()
            ,"Rebounds" : $(tr).find('td:eq(5)').text()
        }
    });
        return TableData;
    }


function addvalues_two() {
    var TableData = new Array();
    $('#add_table').each(function(row,tr){
        TableData[row]={
            "ID" : $(tr).find('td:eq(6)').text()
            ,"PlayerID" : $(tr).find('td:eq(7)').text()
            , "PlayerName" :$(tr).find('td:eq(8)').text()
            , "Points" : $(tr).find('td:eq(9)').text()
            , "Assists" : $(tr).find('td:eq(10)').text()
            ,"Rebounds" : $(tr).find('td:eq(11)').text()
        }
    });
        return TableData;
    }
    function addvalues_three() {
        var TableData = new Array();
        $('#add_table').each(function(row,tr){
            TableData[row]={
                "ID" : $(tr).find('td:eq(12)').text()
                ,"PlayerID" : $(tr).find('td:eq(13)').text()
                , "PlayerName" :$(tr).find('td:eq(14)').text()
                , "Points" : $(tr).find('td:eq(15)').text()
                , "Assists" : $(tr).find('td:eq(16)').text()
                ,"Rebounds" : $(tr).find('td:eq(17)').text()
            }
        });
            return TableData;
        }

        // var button = document.createElement("button");
        // button.innerHTML = "Do Something";

        // // 2. Append somewhere
        // var body = document.getElementsByTagName("body")[0];
        // body.appendChild(button);

        // // 3. Add event handler
        // button.addEventListener ("click", function() {
        //   alert("did something");
        // });


// function Insert_Data() {
//     var table = document.getElementById("del_table");
//     var tr="";
//     TableData.forEach(x=>{
//        tr+='<tr>';
//        tr+='<td>'+x.PlayerID+'</td>'+'<td>'+x.PlayerName+'</td>'+'<td>'+x.Points+'</td>'+'<td>'+x.Assists+'</td>'+'<td>'+x.Rebounds+'</td>'
//        tr+='</tr>'

//     })
//     table.innerHTML+=tr;
//     //Help......
//   }
//  TableData.shift();  // first row is the table header - so remove
function Insert_Data(TableData) {
    var table = document.getElementById("del_table");
    var tr="";
    TableData.forEach(x=>{
       tr+='<tr>';
       tr+='<td>'+x.ID+'<td>'+x.PlayerID+'</td>'+'<td>'+x.PlayerName+'</td>'+'<td>'+x.Points+'</td>'+'<td>'+x.Assists+'</td>'
       tr+='</tr>'

    })
    // var body = document.getElementsById("del_table");
    table.innerHTML+=tr;
    // body.appendChild(button);

  }
function delrow_one(i) {
    var index, table = document.getElementById('del_table');

          table.rows[i].cells[5].onclick = function()
          {
              var c = confirm("Do you want to remove this player?");
              if(c === true)
              {
                  index = this.parentElement.rowIndex;
                  table.deleteRow(index);
                // row = i;
                // var tr="null";
                // var tr="";
                // tr +='<tr>';
                // tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                // tr+='</tr>'
                // table.rows[i].innerHTML = "";
                // table.rows[i].innerHTML = tr;
              }


              //console.log(index);
          };


    }



    function add_elements_one() {
        var add_table = document.getElementById('add_table');


              add_table.rows[2].cells[6].onclick = function()
              {
                  var c = confirm("Do you want to add this player?");
                  if(c === true)
                  {

                      var tab = addvalues_one();
                      Insert_Data(tab);
                      }
                  }

                  //console.log(index);


            }

        function add_elements_two() {
            var add_table = document.getElementById('add_table');


                  add_table.rows[3].cells[6].onclick = function()
                  {
                      var c = confirm("Do you want to add this player?");
                      if(c === true)
                      {

                          var tab = addvalues_two();
                          Insert_Data(tab);
                          }
                      }

                      //console.log(index);
                  };

            function add_elements_three() {
                var add_table = document.getElementById('add_table');


                      add_table.rows[4].cells[6].onclick = function()
                      {
                          var c = confirm("Do you want to add this player?");
                          if(c === true)
                          {

                              var tab = addvalues_three();
                              Insert_Data(tab);
                              }
                          }

                          //console.log(index);
                      };




     delrow_one(2);
     delrow_one(3);
     delrow_one(4);
     delrow_one(5);
     delrow_one(6);
     delrow_one(7);
     delrow_one(8);
     delrow_one(9);
     delrow_one(10);
     delrow_one(11);

    add_elements_one(2);
    add_elements_two(3);
    add_elements_three(4);
