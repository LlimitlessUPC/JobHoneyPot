
import { Injectable, OnInit } from "@angular/core";
import { Http, Headers, Response } from "@angular/http";
import { Observable } from 'rxjs/Observable';

import { User } from "./user";

@Injectable()
export class UserService implements OnInit {
  ngOnInit() {

  }
  constructor(private http: Http) { }
  apply(user: User) {
    let headers = new Headers();

    headers.append("Content-Type", "application/x-www-form-urlencoded");

    const body = "userFirst=" + user.firstName + "&userLast=" + user.lastName + "&dateBirth=" + user.dateBirth
    + "&email=" + user.emailAddress + "&phone=" + user.phoneNumber + "&cv=" + user.cv + "&category=" + user.category;

    return this.http.post('HTTP://127.0.0.1:8000/offer', body, { headers: headers });
  }
}