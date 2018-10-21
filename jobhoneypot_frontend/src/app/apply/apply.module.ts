import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';

import { ApplyComponent } from './apply.component';

import { ComponentsModule } from '../components/components.module';
import { UserService } from 'app/shared/user/user.service';

@NgModule({
    imports: [
        CommonModule,
        BrowserModule,
        FormsModule,
        RouterModule,
        ComponentsModule
    ],
    declarations: [ ApplyComponent ],
    exports:[ ApplyComponent ],
  
})
export class ApplyModule { }
