// removing player from table
//https://www.fourfront.us/blog/store-html-table-data-to-javascript-array/
var TableData = new Array();
$('#add_table').each(function(row, tr){
    TableData[row]={
        "PlayerID" : $(tr).find('td:eq(0)').text()
        , "PlayerName" :$(tr).find('td:eq(1)').text()
        , "Points" : $(tr).find('td:eq(2)').text()
        , "Assists" : $(tr).find('td:eq(3)').text()
        ,"Rebounds" : $(tr).find('td:eq(3)').text()
    }
});

    
// function addval(row) {
// $('#add_table').each(function(tr){
//     var TableData = new Array();
//     TableData[row]={
//         "PlayerId" : $(tr).find('td:eq(0)').text()
//         , "PlayerName" :$(tr).find('td:eq(1)').text()
//         , "Points" : $(tr).find('td:eq(2)').text()
//         , "Assists" : $(tr).find('td:eq(3)').text()
//         ,"Rebounds" : $(tr).find('td:eq(4)').text(),
//         "random" : $(tr).find('td:eq(5)').text()
//     }
// });
//     return Table_Data;
// }
function Insert_Data() {
    var table = document.getElementById("del_table");
    var tr="";
    TableData.forEach(x=>{
       tr+='<tr>';
       tr+='<td>'+x.PlayerID+'</td>'+'<td>'+x.PlayerName+'</td>'+'<td>'+x.Points+'</td>'+'<td>'+x.Assists+'</td>'+'<td>'+x.Rebounds+'</td>'
       tr+='</tr>'
  
    })
    table.innerHTML+=tr;
    //Help......  
  } 
//  TableData.shift();  // first row is the table header - so remove

function delrow() {
    var index, table = document.getElementById('del_table');
      for(var i = 1; i < table.rows.length; i++)
      {
          table.rows[i].cells[5].onclick = function()
          {
              var c = confirm("Do you want to remove this player?");
              if(c === true)
              {
                  index = this.parentElement.rowIndex;
                  table.deleteRow(index);
              }
              
              //console.log(index);
          };
          
        }
    }
    function addr() {
        var add_table = document.getElementById('add_table');
          for(var i = 1; i < add_table.rows.length; i++)
          {
              add_table.rows[i].cells[5].onclick = function()
              {
                  var c = confirm("Do you want to add this player?");
                  if(c === true)
                  {
                      if (del_table.rows.length > 14) {
                          alert("Your team roster must be under 14 people. Please remove the neccessary players to proceed");
                      } else {
                      Insert_Data();
                      }
                  }
                  
                  //console.log(index);
              };
              
            }
        }
    
    delrow();
    addr();
    
    //    function addr() {
    //     var tableRef = document.getElementById('add_table');
    //     var tables = document.getElementById('del_table');
        
    //       tableRef.rows[i].cells[2].onclick = function()
    //       {
    //           var c = confirm("Do you want to add this player?");
    //           if(c === true)
    //           {
    //               tables.insertRow(14);
    //           }
              
    //           //console.log(index);
    //       };
          
    //     }
    
    
