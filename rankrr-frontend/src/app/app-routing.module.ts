import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TextAnalyzerComponent } from './components/text-analyzer/text-analyzer.component';
import { HomeComponent } from './components/home/home.component';
import { RankerComponent } from './components/ranker/ranker.component';
import { RankerDemoComponent } from './components/ranker-demo/ranker-demo.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'demo', component: RankerDemoComponent},
  {path: 'ranker', component: RankerComponent},
  {path: 'text-analyzer', component: TextAnalyzerComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
