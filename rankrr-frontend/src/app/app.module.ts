import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './components/nav/nav.component';
import { TextAnalyzerComponent } from './components/text-analyzer/text-analyzer.component';
import { HomeComponent } from './components/home/home.component';
import { FormsModule } from '@angular/forms';
import { SentimentSummaryBarComponent } from './components/sentiment-summary-bar/sentiment-summary-bar.component';
import { FooterComponent } from './components/footer/footer.component';
import { RankerComponent } from './components/ranker/ranker.component';
import { RankerDemoComponent } from './components/ranker-demo/ranker-demo.component';

import { ToastModule } from 'primeng/toast';
import { MessageService } from 'primeng/api';
import { TableModule } from 'primeng/table';
import { AgGridModule } from 'ag-grid-angular';
import { DialogModule } from 'primeng/dialog';
import { RankedProductsTableComponent } from './components/ranked-products-table/ranked-products-table.component';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    TextAnalyzerComponent,
    HomeComponent,
    SentimentSummaryBarComponent,
    FooterComponent,
    RankerComponent,
    RankerDemoComponent,
    RankedProductsTableComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,

    AgGridModule,
    TableModule,
    ToastModule,
    DialogModule,
  ],
  providers: [MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
