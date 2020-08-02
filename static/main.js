
// removing player from table

function delrow() {
    var index, table = document.getElementById('del_table');
      for(var i = 1; i < table.rows.length; i++)
      {
          table.rows[i].cells[2].onclick = function()
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
        var del_table = document.getElementById('del_table');
          for(var i = 1; i < add_table.rows.length; i++)
          {
              add_table.rows[i].cells[2].onclick = function()
              {
                  var c = confirm("Do you want to add this player?");
                  if(c === true)
                  {
                      del_table.addRow(add_table.rows.length);
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
    
    
    
    
    