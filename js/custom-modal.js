(function ($) {

    'use strict';

    var _parent = $.fn.modal;

    //Here is my constructor

    var Modal = function(element, options){
        _parent.Constructor.apply(this, arguments);

        //put it to console just so we can see
        console.log('modal initialized');

    };

    Modal.DEFAULTS = $.extend({}, _parent.Constructor.DEFAULTS, {backdrop: 'static'});
    Modal.prototype = Object.create(_parent.Constructor.prototype);
    Modal.prototype.parent = function(){
        var args = $.makeArray(arguments),
            method = args.shift();
        _parent.Constructor.prototype[method].apply(this, args)

    };

    Modal.prototype.show = function(){
        this.parent.show();
        //just cause
        console.log('show called');
    };

    $.fn.modal = function(option, _relatedTarget){
        console.log('modal plugin called');
        return this.each(function(){
            var $this = $(this),
                data = $this.data.('bs.modal'),
                options = $.extend({}, Modal.DEFAULTS,
                $this.data(), typeof option === 'object' && option);
            if(!data){
                $this.data('bs.modal', (data = new Modal(this, options)));
            }
            if (typeof option === 'string'){
                data[option](_relatedTarget);
            }else if (options.show){
                data.show(_relatedTarget);
            }
        });
    };
    $.fn.modal.Constructor = Modal;

    $.fn.modal.noConflict = function(){
        $.fn.modal = _parent;
        return this;
    };
})(jQuery);