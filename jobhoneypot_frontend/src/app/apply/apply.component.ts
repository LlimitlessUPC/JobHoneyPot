import { Component, OnInit } from '@angular/core';
import { Http, Headers, Response } from "@angular/http";
import { UserService } from 'app/shared/user/user.service';

@Component({
    selector: 'app-apply',
    templateUrl: './apply.component.html',
    styleUrls: ['./apply.component.scss'] ,
    providers: [
      UserService
  ]
})

export class ApplyComponent implements OnInit {
  focus: any;
  focus1: any;

  constructor(private _userServie: UserService) {}

  ngOnInit() {
    console.log("hollaaa")

  }

  apply(){
    console.log("applying ...")
    this._userServie.apply2().subscribe(res => {
      console.log("res",res)
    }, err => {
      console.log("err",err)

    })
  }
  
}
