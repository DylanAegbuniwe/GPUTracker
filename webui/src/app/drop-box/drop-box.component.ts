import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

export class GPU {
  constructor(
    public datetime: string,
    public gpuname: string,
    public page: number,
    public price: number
  ) {}
   getName(){
    return this.gpuname;
  }
}


@Component({
  selector: 'app-drop-box',
  templateUrl: './drop-box.component.html',
  styleUrls: ['./drop-box.component.css']
  
})
export class DropBoxComponent implements OnInit {
  gpus: GPU[] = [];

  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    this.getGPUs();
  }
  getGPUs(){
    this.httpClient.get<any>('http://127.0.0.1:5000/').subscribe(
      response => {
        console.log(response);
        this.gpus = response
      }
    );
  }
}
