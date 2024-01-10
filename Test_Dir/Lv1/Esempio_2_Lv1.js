
/*COSTRUTTORE BASE*/

var c = document.getElementById("tela");
var draw = c.getContext("2d");

class Vertice
{
    constructor(n, i, xcoor, ycoor)
    {
      if(i === undefined)
      {
        this._nome = n.nome;
        this._x = n.x;
        this._y = n.y;
        this._distStart = n.distStart;
        this._precVert = n.precVert;
        this._index = n.index;
      }
      else
      {
        this._nome = n;
        this._x = xcoor;
        this._y = ycoor;
        this._distStart = 9999;
        this._precVert = "";
        this._index = i;
      } 
    }
    
    show()
    {
      draw.beginPath();
      draw.fillStyle = "#00E600";
      draw.arc(this._x*2.5, this._y*1.8, 15, 0, 2 * Math.PI);
      draw.fill();
      draw.stroke();
      
      draw.fillStyle = "#000000";
      draw.font = "15px Verdana";
      draw.fillText(this._nome, (this._x - 2)*2.5, (this._y+3)*1.8);
    }
    
    set distStart(dist)
    {
        this._distStart = dist;
    }
    
    set precVert(vert)
    {
        this._precVert = vert;
    }
    
    set index(i)
    {
        this._index = i;
    }
    
    get nome()
    {
        return this._nome;
    }
    
    get x()
    {
        return this._x;
    }
    
    get y()
    {
        return this._y;
    }
    
    get distStart()
    {
        return this._distStart;
    }
 
    get precVert()
    {
        return this._precVert.toString();
    }
    
    get index()
    {
        return this._index;
    }
}