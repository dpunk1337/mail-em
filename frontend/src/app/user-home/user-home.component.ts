import { Component } from '@angular/core';

import { Router } from '@angular/router';
import { AuthService } from '@app/auth/auth.service';
import { HttpClient } from '@angular/common/http';
import { LoginComponent } from '@app/auth/login.component';
import { MailService } from '@app/_services/mail.service'

@Component({
  selector: 'app-user-home',
  templateUrl: './user-home.component.html',
  styleUrls: ['./user-home.component.scss']
})
export class UserHomeComponent {

  receiverId : string = "";
  subject : string = "";
  message : string = "";

  constructor(private http: HttpClient, private authService: AuthService, private router: Router, private mailService: MailService) {}

  logOut() {
    this.authService.logout().subscribe(() => {
      this.router.navigate(['/login']);
    });
  }

  onScheduleMail() {
    let mail = {
        'subject': this.subject,
        'message': this.message,
        'sender_id': this.authService.current_user['email'],
        'receiver_id': this.receiverId
    };
    this.mailService.scheduleMail(mail).subscribe(() => {
      alert("Success");
    });
  }
}
