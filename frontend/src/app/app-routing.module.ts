import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './auth/login.component';
import { AuthGuard } from './auth/auth.guard';
import { AdminGuard } from './auth/admin.guard';
import { UserHomeComponent } from '@app/user-home/user-home.component';
import { AdminHomeComponent } from '@app/admin-home/admin-home.component';
import { SignupComponent } from '@app/auth/signup.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'home', component: UserHomeComponent, canActivate: [AuthGuard] },
  { path: 'admin', component: AdminHomeComponent, canActivate: [AuthGuard, AdminGuard] },
  { path: '**', redirectTo: 'home' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
