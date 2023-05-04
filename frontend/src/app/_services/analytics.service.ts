import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '@environments/environment';

@Injectable({ providedIn: 'root' })
export class AnalyticsService {

    constructor(
        private router: Router,
        private http: HttpClient
    ) {

    }

    getMailAnalytics() {
      return this.http.get(`${environment.apiUrl}/mail-analytics`);
    }
}
