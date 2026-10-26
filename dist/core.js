export const LIMITS={count:2000,total:500*1024*1024,hashFile:100*1024*1024};
export function extension(path){const name=path.split('/').pop();const i=name.lastIndexOf('.');return i>0&&i<name.length-1?name.slice(i+1).toLowerCase():'';}
export function hidden(path){return path.split('/').some(p=>p.startsWith('.'));}
export function validateFiles(files){if(!files.length)throw Error('empty');if(files.length>LIMITS.count)throw Error('countLimit');const total=files.reduce((s,f)=>s+f.size,0);if(total>LIMITS.total)throw Error('sizeLimit');return total;}
export function csvCell(value,safe=true){let s=String(value??'');if(safe&&/^[\s]*[=+@-]/.test(s))s="'"+s;return /[",\r\n]/.test(s)?'"'+s.replaceAll('"','""')+'"':s;}
export function csv(rows,safe=true,headers=['경로','확장자','크기(bytes)','수정시각(UTC)','SHA-256']){return [headers,...rows.map(r=>[r.path,r.ext,r.size,r.modified,r.hash])].map(row=>row.map(v=>csvCell(v,safe)).join(',')).join('\r\n')+'\r\n';}
export function mdEscape(v){return String(v).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('\\','\\\\').replaceAll('|','\\|').replaceAll('`','\\`').replace(/\r?\n/g,' ⏎ ');}
export function markdown(rows,labels={title:'폴더 납품 목록',note:'크기 단위: bytes · 수정시각: UTC · SHA-256 빈칸: 미계산',headers:['경로','확장자','크기(bytes)','수정시각(UTC)','SHA-256']}){return '# '+labels.title+'\n\n'+labels.note+'\n\n| '+labels.headers.join(' | ')+' |\n| --- | --- | ---: | --- | --- |\n'+rows.map(r=>'| '+[r.path,r.ext,r.size,r.modified,r.hash].map(mdEscape).join(' | ')+' |').join('\n')+'\n';}
export function formatBytes(n){if(n<1024)return n+' B';return n<1048576?(n/1024).toFixed(1)+' KiB':(n/1048576).toFixed(1)+' MiB';}
export async function digestFile(file,subtle=globalThis.crypto?.subtle){if(!subtle)throw Error('secure');if(file.size>LIMITS.hashFile)throw Error('hashLimit');const digest=await subtle.digest('SHA-256',await file.arrayBuffer());return Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');}
