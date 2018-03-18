+++
draft = false
date="2008-08-10 03:02:47"
title="Controlling window position with the win32 API"
tag=['win32', 'c', 'net']
category=['.NET']
+++

We've been doing a bit of work around controlling the state of the windows of applications launched programmatically.

The problem we were trying to solve is to launch an arbitrary application, move it around the screen and then save its window position on the screen so that next time it's launched it loads in the same position.

There are some win32 APIs designed to do just this, although it took a fair bit of searching and trial and error to work out exactly how to use them.

Since the application we wrote to do this is in C# it was fairly easy to import the win32 APIs, the main method call being <a href="http://msdn.microsoft.com/en-us/library/ms633516(VS.85).aspx">GetWindowInfo</a>, which is imported like so:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>6<tt>
</tt>7<tt>
</tt>8<tt>
</tt>9<tt>
</tt><strong>10</strong><tt>
</tt>11<tt>
</tt>12<tt>
</tt>13<tt>
</tt>14<tt>
</tt>15<tt>
</tt>16<tt>
</tt>17<tt>
</tt>18<tt>
</tt>19<tt>
</tt><strong>20</strong><tt>
</tt>21<tt>
</tt>22<tt>
</tt>23<tt>
</tt>24<tt>
</tt>25<tt>
</tt>26<tt>
</tt>27<tt>
</tt>28<tt>
</tt>29<tt>
</tt><strong>30</strong><tt>
</tt>31<tt>
</tt>32<tt>
</tt>33<tt>
</tt>34<tt>
</tt>35<tt>
</tt>36<tt>
</tt>37<tt>
</tt>38<tt>
</tt>39<tt>
</tt><strong>40</strong><tt>
</tt>41<tt>
</tt>42<tt>
</tt>43<tt>
</tt>44<tt>
</tt>45<tt>
</tt>46<tt>
</tt>47<tt>
</tt>48<tt>
</tt>49<tt>
</tt><strong>50</strong><tt>
</tt>51<tt>
</tt>52<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">   [DllImport(<span class="s"><span class="dl">"</span><span class="k">user32.dll</span><span class="dl">"</span></span>)]<tt>
</tt>   private <span class="r">static</span> <span class="r">extern</span> <span class="pt">bool</span> GetWindowInfo(IntPtr hwnd, ref tagWINDOWINFO pwi); <tt>
</tt><tt>
</tt>   [StructLayout(LayoutKind.Sequential)]<tt>
</tt>    public <span class="r">struct</span> tagRECT<tt>
</tt>    {<tt>
</tt>        <span class="c">/// LONG->int</span><tt>
</tt>        public <span class="pt">int</span> left;<tt>
</tt><tt>
</tt>        <span class="c">/// LONG->int</span><tt>
</tt>        public <span class="pt">int</span> top;<tt>
</tt><tt>
</tt>        <span class="c">/// LONG->int</span><tt>
</tt>        public <span class="pt">int</span> right;<tt>
</tt><tt>
</tt>        <span class="c">/// LONG->int</span><tt>
</tt>        public <span class="pt">int</span> bottom;<tt>
</tt>    }<tt>
</tt><tt>
</tt>    [StructLayout(LayoutKind.Sequential)]<tt>
</tt>    public <span class="r">struct</span> tagWINDOWINFO<tt>
</tt>    {<tt>
</tt>        <span class="c">/// DWORD->unsigned int</span><tt>
</tt>        public uint cbSize;<tt>
</tt><tt>
</tt>        <span class="c">/// RECT->tagRECT</span><tt>
</tt>        public tagRECT rcWindow;<tt>
</tt><tt>
</tt>        <span class="c">/// RECT->tagRECT</span><tt>
</tt>        public tagRECT rcClient;<tt>
</tt><tt>
</tt>        <span class="c">/// DWORD->unsigned int</span><tt>
</tt>        public uint dwStyle;<tt>
</tt><tt>
</tt>        <span class="c">/// DWORD->unsigned int</span><tt>
</tt>        public uint dwExStyle;<tt>
</tt><tt>
</tt>        <span class="c">/// DWORD->unsigned int</span><tt>
</tt>        public uint dwWindowStatus;<tt>
</tt><tt>
</tt>        <span class="c">/// UINT->unsigned int</span><tt>
</tt>        public uint cxWindowBorders;<tt>
</tt><tt>
</tt>        <span class="c">/// UINT->unsigned int</span><tt>
</tt>        public uint cyWindowBorders;<tt>
</tt><tt>
</tt>        <span class="c">/// ATOM->WORD->unsigned short</span><tt>
</tt>        public ushort atomWindowType;<tt>
</tt><tt>
</tt>        <span class="c">/// WORD->unsigned short</span><tt>
</tt>        public ushort wCreatorVersion;<tt>
</tt>    }~~~
</td>
</tr>
</tbody></table>
We found out how to do this from <a href="http://www.pinvoke.net/default.aspx/user32/GetWindowInfo.html">here</a>, but for the sake of explaining how it works I'll keep it here too.

The GetWindowInfo's first argument is a window handler. We launched our application using the .NET Process class so we can access this using the MainWindowHandle property. Don't use WindowHandle as this doesn't get the handle to the window itself - I think it gets the handle to the process which launched the window which is not what we want.

Therefore, to get the position of the window on the screen we can use the following code:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">tagWINDOWINFO info = new tagWINDOWINFO();<tt>
</tt>info.cbSize = (uint)Marshal.SizeOf(info);<tt>
</tt>GetWindowInfo(process.MainWindowHandle, ref info);~~~
</td>
</tr>
</tbody></table>
To put the window back in this position we first need to include the following API calls:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">[DllImport(<span class="s"><span class="dl">"</span><span class="k">user32.dll</span><span class="dl">"</span></span>)]<tt>
</tt>private <span class="r">static</span> <span class="r">extern</span> <span class="pt">bool</span> MoveWindow(IntPtr hWnd, <span class="pt">int</span> X, <span class="pt">int</span> Y, <span class="pt">int</span> nWidth, <span class="pt">int</span> nHeight, <span class="pt">bool</span> bRepaint);<tt>
</tt><tt>
</tt>[DllImport(<span class="s"><span class="dl">"</span><span class="k">user32.dll</span><span class="dl">"</span></span>)]<tt>
</tt>private <span class="r">static</span> <span class="r">extern</span> <span class="pt">bool</span> UpdateWindow(IntPtr hWnd);~~~
</td>
</tr>
</tbody></table>
Then call both of these methods like so:
<table class="CodeRay" border="0">
<tbody>
<tr>
<td class="line_numbers" title="click to toggle" onclick="with (this.firstChild.style) { display = (display == '') ? 'none' : '' }">
<pre>1<tt>
</tt>2<tt>
</tt>3<tt>
</tt>4<tt>
</tt>5<tt>
</tt>~~~
</td>
<td class="code">
<pre ondblclick="with (this.style) { overflow = (overflow == 'auto' || overflow == '') ? 'visible' : 'auto' }">process.Start();<tt>
</tt>process.ForceWaitForInputIdle();<tt>
</tt><tt>
</tt>MoveWindow(process.MainWindowHandle, left, top, width, height, <span class="pc">true</span>);<tt>
</tt>UpdateWindow(process.MainWindowHandle);~~~
</td>
</tr>
</tbody></table>
UpdateWindow needs to be called otherwise the window will remain in its previous position.
