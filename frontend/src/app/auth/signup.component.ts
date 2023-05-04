import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent {
  email: string = "";
  firstName : string = "";
  lastName : string = "";
  password: string = "";

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService.signUp(this.email,this.firstName, this.lastName, this.password).subscribe(() => {
      this.router.navigate(['/home']);
    });
  }
}
