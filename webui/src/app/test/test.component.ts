import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

interface data{
  id: number,
  name: string
}

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.css']
})



export class TestComponent  implements OnInit{

  constructor(){ }

  selectedLevel: any;
  data:Array<data> = [
    {id: 0, name: "name1"},
    {id: 1, name: "name2"}
];

  ngOnInit(): void {
    
  }

  selected(){
    console.log("test:", this.selectedLevel)
  }
 }
