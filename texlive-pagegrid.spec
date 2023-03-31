Name:		texlive-pagegrid
Version:	64470
Release:	2
Summary:	Print page grid in background
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagegrid
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagegrid.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagegrid.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagegrid.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package puts a grid on the paper. It was written for
developers of a class or package who have to put elements on
definite locations on a page (e.g. letter class). The grid
allows a faster optical check, whether the positions are
correct. If the previewer already offers features for
measuring, the package might be unnecessary. Otherwise it saves
the developer from printing the page and measuring by hand. The
package was part of the oberdiek bundle.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pagegrid
%{_texmfdistdir}/tex/latex/pagegrid
%doc %{_texmfdistdir}/doc/latex/pagegrid

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
