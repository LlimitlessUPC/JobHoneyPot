
import { Injectable, OnInit } from "@angular/core";
import { Http, Headers, Response } from "@angular/http";
import { Observable } from 'rxjs/Observable';
import { HttpClient } from '@angular/common/http';

import { User } from "./user";

@Injectable()
export class UserService implements OnInit {
  ngOnInit() {

  }
  constructor(private http: HttpClient) { }
//   apply(user: User) {
//     let headers = new Headers();

//     headers.append("Content-Type", "application/x-www-form-urlencoded");

//     const body = "userFirst=" + user.firstName + "&userLast=" + user.lastName + "&dateBirth=" + user.dateBirth
//     + "&email=" + user.emailAddress + "&phone=" + user.phoneNumber + "&cv=" + user.cv + "&category=" + user.category;

//     return this.http.post('HTTP://127.0.0.1:8000/offers', body, { headers: headers });
//   }
  apply2() {
    console.log("in service")

      let user = {
        "number":1234,
        "type":'issue',
        "action":"show"
     }

    const body = "userFirst=" + user.number + "&userLast=" + user.type + "&dateBirth=" + user.action

    return this.http.post('HTTP://127.0.0.1:8000/offers', body);
  }
}