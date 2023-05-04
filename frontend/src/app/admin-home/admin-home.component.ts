import { Component } from '@angular/core';

import { Router } from '@angular/router';
import { AuthService } from '@app/auth/auth.service';
import { HttpClient } from '@angular/common/http';
import { LoginComponent } from '@app/auth/login.component';
import { AnalyticsService } from '@app/_services/analytics.service'

@Component({
  selector: 'app-admin-home',
  templateUrl: './admin-home.component.html',
  styleUrls: ['./admin-home.component.scss']
})
export class AdminHomeComponent {

  constructor(private http: HttpClient, private authService: AuthService, private router: Router, private analyticsService : AnalyticsService) {}

  logOut() {
    this.authService.logout().subscribe(() => {
      this.router.navigate(['/login']);
    });
  }

  mailAnalytics : any = { 'scheduled' : 0, 'sent' : 0, 'opened' : 0};

  ngOnInit(){
    this.analyticsService.getMailAnalytics().subscribe((response : any) => {
      this.mailAnalytics = response;
    });
  }

}
