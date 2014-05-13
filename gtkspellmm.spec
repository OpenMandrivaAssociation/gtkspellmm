%define api 3.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} %{api} -d

Summary:	On-the-fly spell checking for GtkTextView widgets - C++ bindings
Name:		gtkspellmm
Version:	3.0.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://gtkspell.sourceforge.net/
Source0:	http://sourceforge.net/projects/gtkspell/files/gtkspellmm/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(gtkspell3-3.0)

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	On-the-fly spell checking for GtkTextView widgets - C++ bindings
Group:		System/Libraries

%description -n %{libname}
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package provides header and documentation files for developing C++
applications which use GtkSpell.

%files -n %{devname}
%doc COPYING
%{_includedir}/gtkspellmm-%{api}
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/gtkspellmm-%{api}.pc
%{_libdir}/gtkspellmm-%{api}
%{_datadir}/devhelp/books/gtkspellmm-%{api}
%{_datadir}/doc/gtkspellmm-%{api}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

