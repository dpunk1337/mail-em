import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '@environments/environment';

@Injectable({ providedIn: 'root' })
export class MailService{

    constructor(
        private router: Router,
        private http: HttpClient
    ) {

    }

    scheduleMail(mail : any) {
      let body = new FormData();
      body.append('subject', mail['subject']);
      body.append('message', mail['message']);
      body.append('sender_id', mail['sender_id']);
      body.append('receiver_id', mail['receiver_id']);
      return this.http.post(`${environment.apiUrl}/schedule-mail`, body);
    }

}
