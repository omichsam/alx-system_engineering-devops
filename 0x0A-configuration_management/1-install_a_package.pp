# installs the package flask
package { 'flask':
  ensure   => '2.1.0',cd 
  provider => 'pip3'
}
